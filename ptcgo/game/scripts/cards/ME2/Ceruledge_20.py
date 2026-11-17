from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a7654531-4125-50a0-8bc5-24a6c15db10f",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ceruledge.Name",
    display_name="Ceruledge",
    searchable_by=["Ceruledge", "Stage 1", "Ceruledge"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Attack(
            title="Infernal Slash",
            game_text="Discard 4 Basic Fire Energy cards from your hand. If you can't discard 4 cards in this way, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1},
            damage=220,
            effect=unimplemented,
        ),
    ],
)