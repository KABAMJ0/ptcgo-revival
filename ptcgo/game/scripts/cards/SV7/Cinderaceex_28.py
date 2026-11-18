from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f3a31e86-66dc-5299-90cc-4b68a8d51b3c",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinderaceex.Name",
    display_name="Cinderace ex",
    searchable_by=["Cinderace ex", "Stage 2", "Tera", "ex", "Cinderaceex"],
    subtypes=["Stage 2", "Tera", "ex"],
    collector_number=28,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    family_id=813,
    abilities=[
        Attack(
            title="Flare Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use Flare Strike.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=280,
            effect=unimplemented,
        ),
        Attack(
            title="Garnet Volley",
            game_text="This attack does 180 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
    ],
)