from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.attacks_common import mill_scaled_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d20fe9cc-8874-55b9-9510-6a8c23366822",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkQuilava.Name",
    display_name="Dark Quilava",
    searchable_by=["Dark Quilava", "Stage 1", "DarkQuilava"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name",
    family_id=155,
    abilities=[
        Attack(
            title="Incinerate",
            game_text="Show the top card of your opponent's deck to all players. If it's a Trainer card, discard it.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Rushing Magma",
            game_text="Discard the top 5 cards of your deck. (If there are fewer than 5 cards in your deck, discard all of them.) This attack does 20 damage for each Fire Energy card you discarded in this way.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            damage_operator="x",
            effect=mill_scaled_damage(
                5, 20,
                pred=lambda card: energy_provides_type(
                    card, PokemonTypes.FIRE.value
                ),
            ),
        ),
    ],
)