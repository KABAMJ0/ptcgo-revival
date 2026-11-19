from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.card_effects.attacks_common import bonus_if, has_damage
card = PokemonCardDef(
    guid="d11146d3-1f5c-5437-ab04-f4768acd98ad",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizardex.Name",
    display_name="Charizard ex",
    searchable_by=["Charizard ex", "Stage 2", "ex", "Charizardex"],
    subtypes=["Stage 2", "ex"],
    collector_number=199,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Brave Wing",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(has_damage("self"), 100),
        ),
        Attack(
            title="Explosive Vortex",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 4},
            damage=330,
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)