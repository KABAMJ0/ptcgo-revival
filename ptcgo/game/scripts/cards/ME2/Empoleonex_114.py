from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import (
    attack_effect_shield_passive, protect_next_turn)

card = PokemonCardDef(
    guid="b7ae5001-92c6-5385-9ca9-81aca76a9bf7",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleonex.Name",
    display_name="Empoleon ex",
    searchable_by=["Empoleon ex", "Stage 2", "ex", "Empoleonex"],
    subtypes=["Stage 2", "ex"],
    collector_number=114,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=393,
    abilities=[
        Ability(
            title="Emperor's Stance",
            game_text="Prevent all effects of attacks used by your opponent's Pok\u00e9mon done to this Pok\u00e9mon. (Damage is not an effect.)",
            passive=attack_effect_shield_passive(),
        ),
        Attack(
            title="Iron Feathers",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 60 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=protect_next_turn(reduce=60),
        ),
    ],
)