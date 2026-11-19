from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.passives_common import EnergyTypeRewritePassive

card = PokemonCardDef(
    guid="2b42e487-62cd-5f88-baeb-b4018ad7e1ba",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=79,
    set_code="BW3",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Ability(
            title="Dark Aura",
            game_text="All Energy attached to this Pok\u00e9mon are Darkness Energy instead of their usual type.",
            passive=EnergyTypeRewritePassive(PokemonTypes.DARKNESS.value,
                                             protects="carrier"),
        ),
        Attack(
            title="Berserker Blade",
            game_text="Does 40 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 4},
            damage=60,
            effect=snipe_attack(40, pool="bench", count=2, apply_modifiers=False),
        ),
    ],
)