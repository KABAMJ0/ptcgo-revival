from ptcgo.game.content.definitions import Activations
from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2c666c4c-ddab-5270-8b6b-a25fa3a0df06",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasElectrike.Name",
    display_name="Team Aqua's Electrike",
    searchable_by=["Team Aqua's Electrike", "Basic", "TeamAquasElectrike"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=309,
    abilities=[
        Attack(
            title="Self Charge",
            game_text="Attach an Energy card from your hand to Team Aqua's Electrike.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_hand(target="self", count=1, minimum=1, prompt="Attach an Energy card from your hand"),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)