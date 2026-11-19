from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import mill_per_heads

card = PokemonCardDef(
    guid="57fd1023-3dcd-556c-a581-8f25a22b7e08",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDiglett.Name",
    display_name="Team Rocket's Diglett",
    searchable_by=["Team Rocket's Diglett", "Basic", "TeamRocketsDiglett"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=50,
    abilities=[
        Attack(
            title="Relentless Burrowing",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=mill_per_heads(1, opponent=True),
        ),
    ],
)