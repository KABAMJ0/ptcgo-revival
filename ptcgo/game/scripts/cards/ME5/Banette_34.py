from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import attack_effect_shield_passive
from ptcgo.game.card_effects.trainers import combined, holder_ability_shield

card = PokemonCardDef(
    guid="9fcac721-0e60-5dd8-925b-34eef2ce3fa5",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette", "Stage 1", "Banette"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Ability(
            title="Hide 'n' Sneak",
            game_text="Prevent all effects of your opponent's Pok\u00e9mon's attacks and Abilities done to this Pok\u00e9mon. (Damage is not an effect.)",
            passive=combined(attack_effect_shield_passive(), holder_ability_shield()),
        ),
        Attack(
            title="Puppet Pull",
            game_text="You may search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)