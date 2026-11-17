from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d1dfb516-cdc6-5691-9c39-9a2e9078bc4a",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoex.Name",
    display_name="Tapu Koko ex",
    searchable_by=["Tapu Koko ex", "Basic", "ex", "TapuKokoex"],
    subtypes=["Basic", "ex"],
    collector_number=51,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=785,
    abilities=[
        Attack(
            title="Linked Lightning",
            game_text="This attack does 20 more damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)