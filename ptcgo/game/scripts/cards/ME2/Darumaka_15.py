from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="28c8201b-3e79-587b-ae00-e6e0ac206d5b",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    display_name="Darumaka",
    searchable_by=["Darumaka", "Basic", "Darumaka"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="ME2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=554,
    abilities=[
        Attack(
            title="Blaze Ball",
            game_text="This attack does 20 more damage for each Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)