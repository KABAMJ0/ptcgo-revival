from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_opponent_evolutions

card = PokemonCardDef(
    guid="0ed3a733-550e-5056-807f-92140a85ac98",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Attack(
            title="Evolution Jammer",
            game_text="During your opponent's next turn, they can't play any Pok\u00e9mon from their hand to evolve their Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=lock_opponent_evolutions(),
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)