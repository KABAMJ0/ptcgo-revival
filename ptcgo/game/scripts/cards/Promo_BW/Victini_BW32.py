from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

class _VictoryStarPassive(Passive):
    """After this player flips coins for an attack they may ignore the run and
    flip again; the once-per-turn limit is the turn state's reroll flag."""

    def offers_attack_coin_reroll(self, player_id, carrier):
        pokemon = carrier_pokemon(carrier)
        return pokemon is not None and pokemon.owning_player_id == player_id


card = PokemonCardDef(
    guid="fc8ed3c7-8d44-56c7-9313-020bbda2fc34",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic", "Victini"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
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
            passive=_VictoryStarPassive(),
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