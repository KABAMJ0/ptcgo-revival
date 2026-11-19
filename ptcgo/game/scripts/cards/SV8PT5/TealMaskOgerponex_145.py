from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae3b487e-05df-555f-b82b-9438a13d7fac",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TealMaskOgerponex.Name",
    display_name="Teal Mask Ogerpon ex",
    searchable_by=["Teal Mask Ogerpon ex", "Basic", "Tera", "ex", "TealMaskOgerponex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=145,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1017,
    abilities=[
        Ability(
            title="Teal Dance",
            game_text="Once during your turn, you may attach a Basic Grass Energy card from your hand to this Pok\u00e9mon. If you attached Energy to a Pok\u00e9mon in this way, draw a card.",
            effect=unimplemented,
        ),
        Attack(
            title="Myriad Leaf Shower",
            game_text="This attack does 30 more damage for each Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            damage_operator="+",
            effect=damage_per(lambda c: count_energy("self")(c) + count_energy("defender")(c), 30, base=30),
        ),
    ],
)