from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import subtypes_for
from ptcgo.game.session.passives import Passive


class SealingScreamPassive(Passive):
    """Neither player can play an ACE SPEC card from their hand. Spiritomb need
    not be Active, so there is no position gate."""

    @staticmethod
    def _is_ace_spec(card):
        return any(subtype.lower() == "ace spec" for subtype in
                   subtypes_for(getattr(card, "archetype_id", "") or ""))

    def blocks_trainer_play(self, card, player_id, carrier, board=None):
        return self._is_ace_spec(card)

    def blocks_play(self, player_id, card, carrier, board=None):
        return self._is_ace_spec(card)


card = PokemonCardDef(
    guid="1adae36b-b635-593b-af1f-10f58caa4e1d",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=442,
    abilities=[
        Ability(
            title="Sealing Scream",
            game_text="Each player can't play any ACE SPEC cards from his or her hand.",
            passive=SealingScreamPassive(),
        ),
        Attack(
            title="Hexed Mirror",
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)