from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="6acc9b86-ea45-5af8-9fdc-769d5ab2c4b3",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    display_name="Lileep",
    searchable_by=["Lileep", "Stage 1", "Lileep"],
    subtypes=["Stage 1"],
    collector_number=145,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AntiqueRootFossil.Name",
    family_id=345,
    abilities=[
        Attack(
            title="Bind Down",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=no_retreat_attack(),
        ),
    ],
)