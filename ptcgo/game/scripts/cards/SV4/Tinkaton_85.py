from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack

card = PokemonCardDef(
    guid="e89f61fb-a951-5ce1-ae92-2874385f0d39",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkaton.Name",
    display_name="Tinkaton",
    searchable_by=["Tinkaton", "Stage 2", "Tinkaton"],
    subtypes=["Stage 2"],
    collector_number=85,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    family_id=957,
    abilities=[
        Attack(
            title="Crushing Blow",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=discard_opponent_energy_attack(1),
        ),
        Attack(
            title="Alloyed Hammer",
            game_text="If this Pok\u00e9mon has any Metal Energy attached, this attack does 120 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)