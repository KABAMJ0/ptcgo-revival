from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class _VictoryStarPassive(Passive):
    """After this player flips coins for an attack they may ignore the whole
    run and flip again. The once-per-turn limit is the turn state's
    attack_coin_reroll_used flag, shared with Glimwood Tangle."""

    def offers_attack_coin_reroll(self, player_id, carrier):
        pokemon = carrier_pokemon(carrier)
        return pokemon is not None and pokemon.owning_player_id == player_id


card = PokemonCardDef(
    guid="9128ec3b-5f75-54f9-9ccf-fb7e78fe7a7e",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic", "Victini"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="BW3",
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
            game_text="Once during your turn, after you flip any coins for an attack, you may ignore all effects of those coin flips and being flipping those coins again. You can't use more than 1 Victory Star Ability each turn.",
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