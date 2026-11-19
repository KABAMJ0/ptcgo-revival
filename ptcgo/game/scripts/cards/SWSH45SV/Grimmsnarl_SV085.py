from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per, count_energy
from ptcgo.game.card_effects.passives_common import is_in_active_spot, opposing_active
from ptcgo.game.session.passives import Passive


class DarkOathPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if is_in_active_spot(carrier) and opposing_active(pokemon, carrier):
            cost["Colorless"] = cost.get("Colorless", 0) + 1
        return cost


card = PokemonCardDef(
    guid="dfbbc9de-9e26-5d9c-acea-fc4b0637b1e9",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimmsnarl.Name",
    display_name="Grimmsnarl",
    searchable_by=["Grimmsnarl", "Stage 2", "Grimmsnarl"],
    subtypes=["Stage 2"],
    collector_number=85,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    family_id=859,
    abilities=[
        Ability(
            title="Dark Oath",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Active Pok\u00e9mon's attacks cost Colorless more.",
            passive=DarkOathPassive(),
        ),
        Attack(
            title="Energy Press",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 30, base=100),
        ),
    ],
)