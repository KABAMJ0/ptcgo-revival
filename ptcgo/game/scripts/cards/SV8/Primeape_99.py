from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy

card = PokemonCardDef(
    guid="9bac6450-d594-5596-bd74-bcc06b4d60e1",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    display_name="Primeape",
    searchable_by=["Primeape", "Stage 1", "Primeape"],
    subtypes=["Stage 1"],
    collector_number=99,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Sweep the Leg",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=flip_discard_opponent_energy(),
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)