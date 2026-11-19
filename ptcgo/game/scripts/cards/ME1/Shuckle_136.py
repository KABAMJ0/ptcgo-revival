from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import heal_targets
from ptcgo.game.session.passives import effective_max_hp


def _fermented_juice_condition(board, player_id, pokemon) -> bool:
    if not any(energy_provides_type(energy, PokemonTypes.GRASS.value)
               for energy in board.attached_energies(pokemon)):
        return False
    return any(mon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, mon)
               for mon in board.pokemon_in_play(player_id))


card = PokemonCardDef(
    guid="15701fcf-d261-5cf6-961a-dde36c5ef194",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle", "Basic", "Shuckle"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=213,
    abilities=[
        Ability(
            title="Fermented Juice",
            game_text="Once during your turn, if this Pok\u00e9mon has any Grass Energy attached, you may use this Ability. Heal 30 damage from 1 of your Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=heal_targets(30, scope="choice"),
            condition=_fermented_juice_condition,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)