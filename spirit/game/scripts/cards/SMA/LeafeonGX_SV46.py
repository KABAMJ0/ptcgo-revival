from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e442bdc5-86c9-5f20-b4cf-00388aec014a",
    key="SMA",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonGX.Name",
    display_name="Leafeon-GX",
    searchable_by=["Leafeon-GX", "Stage 1", "GX", "LeafeonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=46,
    set_code="SMA",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Breath of the Leaves",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon, once during your turn (before your attack), you may heal 50 damage from 1 of your Pok\u00e9mon that has any Energy attached to it.",
            effect=unimplemented,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
        Attack(
            title="Grand Bloom-GX",
            game_text="For each of your Benched Basic Pok\u00e9mon, search your deck for a card that evolves from that Pok\u00e9mon and put it onto that Pok\u00e9mon to evolve it. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
    ],
)