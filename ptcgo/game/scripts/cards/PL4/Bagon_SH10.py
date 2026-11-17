from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="31b5760f-65a6-5920-a25c-88d7c7c5e705",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    display_name="Bagon",
    searchable_by=["Bagon", "Basic", "Bagon"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="PL4",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    family_id=371,
    abilities=[
        Ability(
            title="Star Barrier",
            game_text="As long as Bagon has any Energy attached to it, Bagon has no Weakness.",
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Rage",
            game_text="Flip 2 coins. If either of them is tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)