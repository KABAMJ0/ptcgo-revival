from ptcgo.game.card_effects.support_common import search_attach_energy, is_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import attack_grant_passive


def _every_other_pokemon(board, pokemon, carrier):
    return [p for pid in board.player_ids
            for p in board.pokemon_in_play(pid) if p is not pokemon]

card = PokemonCardDef(
    guid="49e5599e-ebf2-5008-a7b8-468262f0231a",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewex.Name",
    display_name="Mew ex",
    searchable_by=["Mew ex", "Basic", "ex", "Mewex"],
    subtypes=["Basic", "ex"],
    collector_number=88,
    set_code="CEL25C",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Versatile",
            game_text="Mew ex can use the attacks of all Pok\u00e9mon in play as its own. (You still need the necessary Energy to use each attack.)",
            passive=attack_grant_passive(_every_other_pokemon),
        ),
        Attack(
            title="Power Move",
            game_text="Search your deck for an Energy card and attach it to Mew ex. Shuffle your deck afterward. Then, you may switch Mew ex with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=search_attach_energy(predicate=is_energy, count=1, to_self=True),
        ),
    ],
)