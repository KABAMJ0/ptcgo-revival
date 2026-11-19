from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import Passive, is_in_active_spot
from ptcgo.game.session.passives import carrier_pokemon

class _ActiveAbilityLock(Passive):
    """While the carrier is the Active Pokemon, no Pokemon in play can use
    its Poke-Powers."""

    def blocks_abilities(self, pokemon, carrier):
        return is_in_active_spot(carrier_pokemon(carrier))


card = PokemonCardDef(
    guid="60f7459d-84e6-583c-84dd-735ebd7828df",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Muk"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Stench",
            game_text="As long as Muk is your Active Pok\u00e9mon, each player's Pok\u00e9mon can't use any Pok\u00e9-Powers.",
            passive=_ActiveAbilityLock(),
        ),
        Attack(
            title="Poison Ring",
            game_text="The Defending Pok\u00e9mon is now Poisoned. The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Sludge Toss",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)