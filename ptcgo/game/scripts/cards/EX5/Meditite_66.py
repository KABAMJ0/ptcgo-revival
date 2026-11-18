from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f2095435-23eb-5017-bda2-f6a036707171",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    display_name="Meditite",
    searchable_by=["Meditite", "Basic", "Meditite"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=307,
    abilities=[
        Attack(
            title="Jab",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Steady Punch",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(30)),
        ),
    ],
)