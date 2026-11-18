from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import (
    count_discard,
    damage_per,
    self_energy_discard_attack,
)
from ptcgo.game.card_effects.pokemon import energy_provides_type, is_energy_card


def _is_fire_energy_card(card) -> bool:
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)

card = PokemonCardDef(
    guid="d64e09fa-2b87-595d-bfbd-6de809a1582e",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonGX.Name",
    display_name="Flareon-GX",
    searchable_by=["Flareon-GX", "Stage 1", "GX", "FlareonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=171,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Heat Stage",
            game_text="You may attach up to 3 Fire Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=self_energy_discard_attack(2, energy_type=PokemonTypes.FIRE),
        ),
        Attack(
            title="Power Burner-GX",
            game_text="This attack does 20 damage for each Fire Energy card in your discard pile. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_discard("mine", _is_fire_energy_card), 20),
        ),
    ],
)