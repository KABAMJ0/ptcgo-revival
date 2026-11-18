from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import (
    self_energy_discard_attack,
    snipe_attack,
)
from ptcgo.game.card_effects.passives_common import retreat_free_when


def _no_retreat_for_non_gx(pokemon, carrier) -> bool:
    if pokemon.owning_player_id != carrier.owning_player_id:
        return False
    subtypes = subtypes_for(pokemon.archetype_id)
    return "GX" not in subtypes and "EX" not in subtypes

card = PokemonCardDef(
    guid="65016ed8-db8e-5ff2-aab0-94f787cd7ee7",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SalamenceGX.Name",
    display_name="Salamence-GX",
    searchable_by=["Salamence-GX", "Stage 2", "GX", "SalamenceGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=139,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=373,
    abilities=[
        Ability(
            title="Dragon Lift",
            game_text="Your Pok\u00e9mon in play have no Retreat Cost, except Pok\u00e9mon-GX and Pok\u00e9mon-EX.",
            passive=retreat_free_when(_no_retreat_for_non_gx),
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=self_energy_discard_attack(2),
        ),
        Attack(
            title="Flame Jet-GX",
            game_text="This attack does 120 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(120, pool="any", count=1),
        ),
    ],
)