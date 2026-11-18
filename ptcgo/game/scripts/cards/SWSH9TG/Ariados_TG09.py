from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="86744baf-3b8e-58d3-9e9e-361b7057c32b",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1", "Ariados"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="SWSH9TG",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=168,
    abilities=[
        Ability(
            title="Spider Net",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may switch 1 of your opponent's Benched Evolution Pok\u00e9mon with their Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Poison Sting",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)