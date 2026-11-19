from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon

class _EffectShield(Passive):
    """Opposing attacks' effects do nothing to this Pokemon; damage is not an
    effect, so the damage pipeline is untouched."""

    def blocks_attack_effects(self, target, carrier):
        return target is carrier_pokemon(carrier)

card = PokemonCardDef(
    guid="6056c5b7-6dfb-53aa-a7e9-eafaf8d5f35d",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon",
    searchable_by=["Charmeleon", "Stage 1", "Charmeleon"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Flare Veil",
            game_text="Prevent all effects of attacks used by your opponent's Pok\u00e9mon done to this Pok\u00e9mon. (Damage is not an effect.)",
            passive=_EffectShield(),
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
        ),
    ],
)