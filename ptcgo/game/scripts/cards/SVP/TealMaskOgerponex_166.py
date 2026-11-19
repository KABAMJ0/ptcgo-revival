from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="248f5916-eef5-52ff-a58c-8e5d518cdcde",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TealMaskOgerponex.Name",
    display_name="Teal Mask Ogerpon ex",
    searchable_by=["Teal Mask Ogerpon ex", "Basic", "Tera", "ex", "TealMaskOgerponex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=166,
    set_code="SVP",
    rarity=Rarities.RarePromo,
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