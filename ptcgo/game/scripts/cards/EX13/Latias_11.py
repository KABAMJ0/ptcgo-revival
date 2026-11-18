from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b8d2917-1fab-5892-97ce-5874cad7a373",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias δ",
    searchable_by=["Latias \u03b4", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=380,
    abilities=[
        Ability(
            title="Dual Aura",
            game_text="As long as you have Latios or Latios ex in play, each player's Evolved Pok\u00e9mon (excluding Pok\u00e9mon-ex) can't use any Pok\u00e9-Bodies.",
            effect=unimplemented,
        ),
        Attack(
            title="Spearhead",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)