from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import (
    attacker_has_energy_at_most, attack_shield_from, carrier_pokemon,
    is_in_active_spot,
)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e4f7447d-e005-5135-9557-fdedcf7fba80",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name",
    display_name="Bastiodon",
    searchable_by=["Bastiodon", "Stage 2", "Bastiodon"],
    subtypes=["Stage 2"],
    collector_number=93,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    family_id=410,
    abilities=[
        Ability(
            title="Ancient Bulwark",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage done to each of your Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon that have 2 or less Energy attached.",
            passive=attack_shield_from(
                attacker_has_energy_at_most(2), protects="team",
                when=lambda board, carrier: not is_in_active_spot(
                    carrier_pokemon(carrier) or carrier)),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)