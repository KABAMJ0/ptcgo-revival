from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7eae81ae-5447-5a69-b306-6697b76b1b21",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricityex.Name",
    display_name="Toxtricity ex",
    searchable_by=["Toxtricity ex", "Stage 1", "Tera", "ex", "Toxtricityex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=100,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Attack(
            title="Knocking Hammer",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=70,
            effect=unimplemented,
        ),
        Attack(
            title="Gaia Punk",
            game_text="Discard 3 Lightning Energy from your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=270,
            effect=unimplemented,
        ),
    ],
)