from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy

card = PokemonCardDef(
    guid="2e59bf60-b33a-5043-a96c-6febc13e43f3",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    display_name="Rhydon",
    searchable_by=["Rhydon", "Stage 1", "Rhydon"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Destructive Horn",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=flip_discard_opponent_energy(),
        ),
    ],
)