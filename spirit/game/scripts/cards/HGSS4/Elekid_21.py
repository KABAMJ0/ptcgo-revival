from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="64fee633-2f17-5b12-a74f-124ca180d90c",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elekid.Name",
    display_name="Elekid",
    searchable_by=["Elekid", "Basic", "Elekid"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=239,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Elekid is Asleep, prevent all damage done to Elekid by attacks.",
            effect=unimplemented,
        ),
        Attack(
            title="Sparking Ball",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance. Elekid is now Asleep.",
            cost={},
            effect=unimplemented,
        ),
    ],
)