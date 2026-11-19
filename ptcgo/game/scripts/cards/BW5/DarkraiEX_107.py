from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.passives_common import retreat_free_when
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.models.board import BoardState


def _dark_cloak_target(pokemon, carrier):
    return (pokemon.owning_player_id == carrier.owning_player_id
            and any(energy_provides_type(e, PokemonTypes.DARKNESS.value)
                    for e in BoardState.attached_energies(pokemon)))

card = PokemonCardDef(
    guid="f19afb86-1902-5c87-a8aa-982c26240702",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiEX.Name",
    display_name="Darkrai-EX",
    searchable_by=["Darkrai-EX", "Basic", "EX", "DarkraiEX"],
    subtypes=["Basic", "EX"],
    collector_number=107,
    set_code="BW5",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=491,
    abilities=[
        Ability(
            title="Dark Cloak",
            game_text="Each of your Pok\u00e9mon that has any Darkness Energy attached to it has no Retreat Cost.",
            passive=retreat_free_when(_dark_cloak_target),
        ),
        Attack(
            title="Night Spear",
            game_text="Does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=snipe_attack(30, pool="bench", count=1, apply_modifiers=False),
        ),
    ],
)