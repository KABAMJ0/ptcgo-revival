from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import named_in_play, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

async def iceberg_crush(ctx):
    if not _named_in_play("Regirock ex")(ctx):
        return
    results = await ctx.flip_coins(1, "Iceberg Crush")
    if results and results[0]:
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.discard_energy_from(
                defender, 1, prompt="Discard an Energy card from the Defending Pokémon")

def _named_in_play(name, side="mine"):
    """Printed-name test: the corpus stores EVOLUTION_LOGIC_NAME without the
    space ("Regirockex"), so a literal `named_in_play("Regirock ex")` is false
    forever. Compare the display name instead."""
    from ptcgo.game.content.definitions import def_for

    def cond(ctx):
        pool = (ctx.my_pokemon_in_play() if side == "mine"
                else ctx.opponent_pokemon_in_play())
        for pokemon in pool:
            definition = def_for(pokemon.archetype_id)
            if definition is not None and definition.display_name == name:
                return True
        return False
    return cond


card = PokemonCardDef(
    guid="dccd490d-be29-5be2-975e-c279925f66a3",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regiceex.Name",
    display_name="Regice ex",
    searchable_by=["Regice ex", "Basic", "ex", "Regiceex"],
    subtypes=["Basic", "ex"],
    collector_number=98,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=378,
    abilities=[
        Attack(
            title="Ice Beam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Iceberg Crush",
            game_text="If Regirock ex is in play, flip a coin. If heads, discard 1 Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=iceberg_crush,
        ),
    ],
)