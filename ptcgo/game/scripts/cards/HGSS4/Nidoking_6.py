from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import Passive
from ptcgo.game.data_utils import def_for
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

class _PheromoneStamina(Passive):
    """+20 max HP per Nidoqueen this Nidoking's owner has in play."""

    def max_hp_bonus(self, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return 0
        return 20 * sum(
            1 for p in board.pokemon_in_play(pokemon.owning_player_id)
            if (def_for(p.archetype_id or "").display_name or "") == "Nidoqueen")

card = PokemonCardDef(
    guid="2903b0c1-a8c3-5f35-aa63-8223a89b2aec",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="HGSS4",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Ability(
            title="Pheromone Stamina",
            game_text="Nidoking gets +20 HP for each Nidoqueen you have in play.",
            passive=_PheromoneStamina(),
        ),
        Attack(
            title="Venomous Horn",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
