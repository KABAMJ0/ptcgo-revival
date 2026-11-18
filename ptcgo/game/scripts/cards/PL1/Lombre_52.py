from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9ee9bbb-1c91-55bc-8455-e75e3c77c7a5",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    display_name="Lombre",
    searchable_by=["Lombre", "Stage 1", "Lombre"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name",
    family_id=270,
    abilities=[
        Attack(
            title="Interrupt",
            game_text="Flip a coin. If heads, look at your opponent's hand and choose 1 card, then have your opponent shuffle that card into his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)