from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d4615668-4545-520a-bd8b-867700ba7c28",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name",
    display_name="Uxie",
    searchable_by=["Uxie", "Basic", "Uxie"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=480,
    abilities=[
        Ability(
            title="Secret Territory",
            game_text="If you have Mesprit and Azelf in play, apply Weakness for each Pok\u00e9mon (both yours and your opponent's) as \u00d74 instead.",
            effect=unimplemented,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)