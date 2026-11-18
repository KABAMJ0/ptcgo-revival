from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c12de612-aced-59aa-b98d-bbbd69428703",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name",
    display_name="Thundurus",
    searchable_by=["Thundurus", "Basic", "Thundurus"],
    subtypes=["Basic"],
    collector_number=139,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=642,
    abilities=[
        Ability(
            title="Adverse Weather",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, prevent all damage done to your Benched Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Gigantic Bolt",
            game_text="This Pok\u00e9mon also does 90 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)