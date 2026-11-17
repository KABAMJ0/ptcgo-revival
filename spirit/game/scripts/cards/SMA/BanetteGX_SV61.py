from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9c1eb693-20a3-5ae0-a1ac-1e1defea1eac",
    key="SMA",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BanetteGX.Name",
    display_name="Banette-GX",
    searchable_by=["Banette-GX", "Stage 1", "GX", "BanetteGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=61,
    set_code="SMA",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Ability(
            title="Shady Move",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may move 1 damage counter from 1 Pok\u00e9mon to another Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Chant",
            game_text="This attack does 10 more damage for each Supporter card in your discard pile. You can't add more than 100 damage in this way.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Tomb Hunt-GX",
            game_text="Put 3 cards from your discard pile into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)