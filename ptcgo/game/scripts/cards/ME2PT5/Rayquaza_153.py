from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if


def _entered_active_this_turn(ctx):
    return ctx.entered_active_this_turn(ctx.attacker)


card = PokemonCardDef(
    guid="35f851d0-b6b6-595b-93aa-bf127a3268ca",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=153,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=384,
    abilities=[
        Attack(
            title="Breakthrough Assault",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack does 90 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_entered_active_this_turn, 90),
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)