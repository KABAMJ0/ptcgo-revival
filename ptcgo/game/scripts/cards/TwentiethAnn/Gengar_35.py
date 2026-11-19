from ptcgo.game.card_effects.attacks_common import condition_attack, spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
card = PokemonCardDef(
    guid="af12b504-3efa-5f74-9427-58dc78712ee7",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=35,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Sinister Fog",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 1 damage counter on each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.POISONED, also=spread_damage(10, side="opponent")),
        ),
        Attack(
            title="Creep Show",
            game_text="If your opponent's Active Pok\u00e9mon has 3 or more damage counters on it, that Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)