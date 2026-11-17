from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2b71dbb3-c574-599a-b106-fa18b30b9763",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TyranitarEX.Name",
    display_name="Tyranitar-EX",
    searchable_by=["Tyranitar-EX", "Basic", "EX", "TyranitarEX"],
    subtypes=["Basic", "EX"],
    collector_number=42,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=248,
    abilities=[
        Attack(
            title="Hammer In",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Break Ground",
            game_text="This attack does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=unimplemented,
        ),
    ],
)