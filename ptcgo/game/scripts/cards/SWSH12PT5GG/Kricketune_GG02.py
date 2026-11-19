from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive


class SwellingTunePassive(Passive):
    stacking_key = "SwellingTune"

    def max_hp_bonus(self, pokemon, carrier, board=None):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return 0
        if pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Kricketune":
            return 0
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.GRASS.value not in types:
            return 0
        return 40


card = PokemonCardDef(
    guid="a61b5848-8463-5098-9e9c-0e1fc9052aab",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketune.Name",
    display_name="Kricketune",
    searchable_by=["Kricketune", "Stage 1", "Kricketune"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name",
    family_id=401,
    abilities=[
        Ability(
            title="Swelling Tune",
            game_text="Your Grass Pokémon in play, except any Kricketune, get +40 HP. You can't apply more than 1 Swelling Tune Ability at a time.",
            passive=SwellingTunePassive(),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)