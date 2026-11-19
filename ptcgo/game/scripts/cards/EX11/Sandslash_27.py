from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, damage_counters_on
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import is_pokemon_ex


async def _delta_storm(ctx):
    """Checkup counters while Sandslash is the Active: 1 on each of the
    opponent's Pokemon-ex."""
    if ctx.source is None or not is_in_active_spot(ctx.source):
        return
    for pokemon in ctx.opponent_pokemon_in_play():
        if is_pokemon_ex(pokemon):
            await ctx.deal_damage(10, target=pokemon, as_counters=True)


card = PokemonCardDef(
    guid="21a18ccb-fb75-5d09-9fbe-135d86bb15f6",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name",
    display_name="Sandslash δ",
    searchable_by=["Sandslash \u03b4", "Stage 1", "Sandslash"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    family_id=27,
    abilities=[
        Ability(
            title="Delta Storm",
            game_text="As long as Sandslash is your Active Pok\u00e9mon, put 1 damage counter on each of your opponent's Pok\u00e9mon-ex between turns.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=_delta_storm,
        ),
        Attack(
            title="Rend",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(lambda ctx: damage_counters_on("defender")(ctx) > 0, 20),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)