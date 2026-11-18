from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="956057a9-1cdd-5000-ad2d-4482318986c1",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronValiant.Name",
    display_name="Iron Valiant",
    searchable_by=["Iron Valiant", "Basic", "Future", "IronValiant"],
    subtypes=["Basic", "Future"],
    collector_number=79,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=1006,
    abilities=[
        Attack(
            title="Gemini Laser",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Zen Blade",
            game_text="During your next turn, this Pok\u00e9mon can't use Zen Blade.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)