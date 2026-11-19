from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

from ptcgo.game.card_effects.support_common import switch_self_attack

_teleport_blast = switch_self_attack(optional=True)

card = PokemonCardDef(
    guid="172c5580-828b-5384-baab-e319daa7dd86",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkAlakazam.Name",
    display_name="Dark Alakazam",
    searchable_by=["Dark Alakazam", "Stage 2", "DarkAlakazam"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="BASE5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkKadabra.Name",
    family_id=63,
    abilities=[
        Attack(
            title="Teleport Blast",
            game_text="You may switch Dark Alakazam with 1 of your Benched Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_teleport_blast,
        ),
        Attack(
            title="Mind Shock",
            game_text="Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=40,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)