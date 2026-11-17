from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="637e454f-b5db-5621-995d-bac86e846b99",
    key="SMP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArmoredMewtwo.Name",
    display_name="Armored Mewtwo",
    searchable_by=["Armored Mewtwo", "Basic", "ArmoredMewtwo"],
    subtypes=["Basic"],
    collector_number=228,
    set_code="SMP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Psychic Raid",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)