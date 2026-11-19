from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class VictoryStarPassive(Passive):
    """Once during your turn, after you flip any coins for an attack, you may
    ignore them and flip again. It is not limited to the Active spot (unlike
    Trick Coin), so any Victini with this Ability in play offers it."""

    def offers_attack_coin_reroll(self, player_id, carrier):
        pokemon = carrier_pokemon(carrier)
        return pokemon is not None and pokemon.owning_player_id == player_id


card = PokemonCardDef(
    guid="e088d63c-8d63-5698-9ee9-50cc74722947",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic", "Victini"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Ability(
            title="Victory Star",
            game_text="Once during your turn, after you flip any coins for an attack, you may ignore all effects of those coin flips and begin flipping those coins again. You can't use more than 1 Victory Star Ability each turn.",
            passive=VictoryStarPassive(),
        ),
        Attack(
            title="Stored Power",
            game_text="Move all Energy attached to this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)