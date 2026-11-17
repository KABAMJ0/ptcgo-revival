from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="82535574-9cf4-5102-a22b-50359067e382",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoochum.Name",
    display_name="Smoochum",
    searchable_by=["Smoochum", "Basic", "Smoochum"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=238,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Smoochum is Asleep, prevent all damage done to Smoochum by attacks.",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Antics",
            game_text="Move an Energy card attached to 1 of your opponent's Pok\u00e9mon to another of your opponent's Pok\u00e9mon. Smoochum is now Asleep.",
            cost={},
            effect=unimplemented,
        ),
    ],
)