from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e3c812a5-fb90-5a1a-ae70-a6fce31a6a1f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysKomala.Name",
    display_name="Larry's Komala",
    searchable_by=["Larry's Komala", "Basic", "LarrysKomala"],
    subtypes=["Basic"],
    collector_number=175,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=775,
    abilities=[
        Ability(
            title="Lethargic Charge",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, you may use this Ability. Attach an Energy card from your hand to your Active Larry's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Dozing Draw",
            game_text="This Pok\u00e9mon is now Asleep. Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)